package com.example.bugfixer.controller;

import com.example.bugfixer.model.CodeAnalysisResult;
import com.example.bugfixer.model.CodeRequest;
import com.example.bugfixer.service.AIService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/code")
public class CodeAnalysisController {

    @Autowired
    private AIService aiService;

    @PostMapping("/analyze")
    public ResponseEntity<?> analyzeCode(@RequestBody CodeRequest request) {
        try {
            CodeAnalysisResult result = aiService.analyze(request.getLanguage(), request.getCode());
            return ResponseEntity.ok(result);
        } catch (Exception e) {
            e.printStackTrace(); // Print to console
            return ResponseEntity.status(500).body("Internal Server Error: " + e.getMessage());
        }
    }

}
