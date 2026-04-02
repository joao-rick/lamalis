package com.example.validador.model;

import jakarta.persistence.*;

@Entity
@Table(name = "regras_validacao")
public class RegraValidacao {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String categoria;
    private Double valorMinimo;

    public String getCategoria() {
        return categoria;
    }

    public Double getValorMinimo() {
        return valorMinimo;
    }
}
