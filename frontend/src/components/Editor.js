import React, { useState } from 'react';
import Editor from '@monaco-editor/react';
import axios from 'axios';

const CodeEditor = () => {
    const [code, setCode] = useState("");
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    const handleAnalyze = async () => {
        setLoading(true);
        setError("");
        setResult(null);

        try {
            const response = await axios.post('http://localhost:5000/analyze', {
                language: "java",
                code: code
            });

            setResult(response.data);
        } catch (err) {
            console.error("❌ Error analyzing code:", err);
            if (err.response?.data?.error) {
                setError(`Server Error: ${err.response.data.error}`);
            } else {
                setError(`Network Error: ${err.message}`);
            }
        } finally {
            setLoading(false);
        }
    };

    return (
        <div style={{ padding: "20px", fontFamily: "Arial" }}>
            <Editor
                height="400px"
                language="java"
                value={code}
                onChange={(value) => setCode(value || "")}
                theme="vs-dark"
            />
            <button onClick={handleAnalyze} style={{
                marginTop: "10px",
                padding: "10px 20px",
                backgroundColor: "#2196f3",
                color: "#fff",
                border: "none",
                borderRadius: "5px",
                cursor: "pointer"
            }}>
                Analyze Code
            </button>

            {loading && <p>⏳ Analyzing...</p>}
            {error && <p style={{ color: "red" }}>❌ {error}</p>}

            {result && (
                <div style={{
                    marginTop: "20px",
                    background: "#1e1e1e",
                    padding: "20px",
                    borderRadius: "10px",
                    color: "#f1f1f1",
                    fontFamily: "Consolas, monospace",
                    boxShadow: "0 4px 8px rgba(0,0,0,0.3)"
                }}>
                    <h3 style={{ color: "#ffd700" }}>🛠️ Issues</h3>
                    <ul>
                        {Array.isArray(result.issues) && result.issues.length > 0
                            ? result.issues.map((issue, i) => (
                                <li key={i}>{issue.replace(/^- /, "").trim()}</li>
                            ))
                            : <li>No issues found.</li>}
                    </ul>

                    <h3 style={{ color: "#00e676" }}>💡 Suggestions</h3>
                    <ul>
                        {Array.isArray(result.suggestions) && result.suggestions.length > 0
                            ? result.suggestions.map((s, i) => (
                                <li key={i}>{s.replace(/^- /, "").trim()}</li>
                            ))
                            : <li>No suggestions available.</li>}
                    </ul>

                    <h3 style={{ color: "#64b5f6" }}>🔧 Fixed Code</h3>
                    <pre style={{
                        background: "#2d2d2d",
                        padding: "10px",
                        borderRadius: "5px",
                        overflowX: "auto",
                        whiteSpace: "pre-wrap"
                    }}>
                        {result.fixedCode?.trim() || "No fixed code provided."}
                    </pre>
                </div>
            )}
        </div>
    );
};

export default CodeEditor;
