package com.example.validador.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Data;


public class CriptoDTO {
    @JsonProperty("nome_criptomoeda")
    private String nomeCriptomoeda;

    private String sigla;

    @JsonProperty("valor_atual")
    private Double valorAtual;

    @JsonProperty("valor_inicial")
    private Double valorInicial;

    @JsonProperty("nivel_risco")
    private String nivelRisco;


    public String getNomeCriptomoeda() {
        return nomeCriptomoeda;
    }

    public void setNomeCriptomoeda(String nomeCriptomoeda) {
        this.nomeCriptomoeda = nomeCriptomoeda;
    }

    public String getSigla() {
        return sigla;
    }

    public Double getValorAtual() {
        return valorAtual;
    }

    public void setValorAtual(Double valorAtual) {
        this.valorAtual = valorAtual;
    }

    public Double getValorInicial() {
        return valorInicial;
    }

    public void setValorInicial(Double valorInicial) {
        this.valorInicial = valorInicial;
    }

    public void setSigla(String sigla) {
        this.sigla = sigla;
    }

    public String getNivelRisco() {
        return nivelRisco;
    }

    public void setNivelRisco(String nivelRisco) {
        this.nivelRisco = nivelRisco;
    }
}