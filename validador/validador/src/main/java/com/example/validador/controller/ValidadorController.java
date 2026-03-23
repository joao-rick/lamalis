package com.example.validador.controller;

import com.example.validador.dto.CriptoDTO;
import com.example.validador.service.MarketCapService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/v1/validar")
public class ValidadorController {

    @Autowired
    private MarketCapService service;

    @PostMapping
    public Map<String, Object> validar(@RequestBody CriptoDTO dados) {
        Map<String, Object> analise = service.processarAnalise(dados);

        Map<String, Object> resposta = new HashMap<>();
        resposta.put("nome", dados.getNomeCriptomoeda());
        resposta.put("sigla", dados.getSigla());
        resposta.put("analise", analise);

        return resposta;
    }
}