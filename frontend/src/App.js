import React from 'react';
import CodeEditor from './components/Editor';

function App() {
    return (
        <div style={{ minHeight: "100vh", display: "flex", flexDirection: "column" }}>
            <div style={{ flex: 1 }}>
                <h1>AI Bug Fix & Suggestion Tool</h1>
                <CodeEditor />
            </div>

            <footer style={{
                textAlign: "center",
                padding: "10px 0",
                backgroundColor: "#f1f1f1",
                color: "#333",
                position: "fixed",
                bottom: 0,
                left: 0,
                width: "100%",
                boxShadow: "0 -1px 5px rgba(0,0,0,0.1)"
            }}>
                Created & Owned by Joshua V
            </footer>
        </div>
    );
}

export default App;
