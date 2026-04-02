package com.example.validador.service;

import com.example.validador.dto.CriptoDTO;
import com.example.validador.model.RegraValidacao;
import com.example.validador.repository.RegraRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.HashMap;
import java.util.Map;

@Service
public class MarketCapService {

    @Autowired
    private RegraRepository repository;

    public Map<String, Object> processarAnalise(CriptoDTO dados) {
        RegraValidacao regraLC = repository.findByCategoria("LC");
        RegraValidacao regraMC = repository.findByCategoria("MC");

        double variacao = ((dados.getValorAtual() - dados.getValorInicial()) / dados.getValorInicial()) * 100;

        String categoriaResultado;

        // Classificação de Market Cap
        if (dados.getValorAtual() > regraLC.getValorMinimo() || "Low".equalsIgnoreCase(dados.getNivelRisco())) {
            categoriaResultado = "LC (Large Cap)";
        }
        else if (dados.getValorAtual() > regraMC.getValorMinimo()) {
            categoriaResultado = "MC (Mid Cap)";
        }
        else {
            categoriaResultado = "SC (Small Cap)";
        }

        Map<String, Object> resultado = new HashMap<>();
        resultado.put("marketCap", categoriaResultado);
        resultado.put("valorizacaoPercentual", String.format("%.2f%%", variacao));

        return resultado;
    }
}