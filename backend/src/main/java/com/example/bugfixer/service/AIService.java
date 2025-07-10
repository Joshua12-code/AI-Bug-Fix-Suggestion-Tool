package com.example.bugfixer.service;

import com.example.bugfixer.model.CodeAnalysisResult;
import java.util.*;
import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class AIService {

    public CodeAnalysisResult analyze(String language, String code) {
        RestTemplate restTemplate = new RestTemplate();
        String url = "http://localhost:5000/analyze";

        // Prepare request
        Map<String, String> requestMap = new HashMap<>();
        requestMap.put("language", language);
        requestMap.put("code", code);

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        HttpEntity<Map<String, String>> requestEntity = new HttpEntity<>(requestMap, headers);

        // Use response as Map first to avoid deserialization issues
        ResponseEntity<Map> response = restTemplate.exchange(
                url,
                HttpMethod.POST,
                requestEntity,
                Map.class
        );

        Map<String, Object> responseBody = response.getBody();

        // Manually construct CodeAnalysisResult
        CodeAnalysisResult result = new CodeAnalysisResult();

        if (responseBody != null) {
            result.setIssues((List<String>) responseBody.get("issues"));
            result.setSuggestions((List<String>) responseBody.get("suggestions"));
            result.setUnitTest((String) responseBody.get("unitTest"));
        }

        return result;
    }
}
