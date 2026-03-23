package com.example.validador.service;

import com.example.validador.dto.CriptoDTO;
import org.springframework.stereotype.Service;
import java.util.HashMap;
import java.util.Map;

@Service
public class MarketCapService {

    public Map<String, Object> processarAnalise(CriptoDTO dados) {
        // Cálculo do percentual de valorização
        double variacao = ((dados.getValorAtual() - dados.getValorInicial()) / dados.getValorInicial()) * 100;

        // Classificação de Market Cap
        String categoria;
        if (dados.getValorAtual() > 80000 || "Low".equalsIgnoreCase(dados.getNivelRisco())) {
            categoria = "LC (Large Cap)";
        } else if (dados.getValorAtual() > 40000) {
            categoria = "MC (Mid Cap)";
        } else {
            categoria = "SC (Small Cap)";
        }

        Map<String, Object> resultado = new HashMap<>();
        resultado.put("marketCap", categoria);
        resultado.put("valorizacaoPercentual", String.format("%.2f%%", variacao));

        return resultado;
    }
}