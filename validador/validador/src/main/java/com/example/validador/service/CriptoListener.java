package com.example.validador.service;

import com.example.validador.dto.CriptoDTO;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import java.util.Map;

@Component
public class CriptoListener {

    @Autowired
    private MarketCapService marketCapService;

    @RabbitListener(queues = "cripto_queue")
    public void consumirMensagem(CriptoDTO dados) {
        Map<String, Object> analise = marketCapService.processarAnalise(dados);

        System.out.println("Mensagem recebida do RabbitMQ!");
        System.out.println("Cripto: " + dados.getNomeCriptomoeda());
        System.out.println("Resultado da Análise: " + analise);
    }
}