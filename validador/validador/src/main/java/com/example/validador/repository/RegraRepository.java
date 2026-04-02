package com.example.validador.repository;

import com.example.validador.model.RegraValidacao;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface RegraRepository extends JpaRepository<RegraValidacao, Long> {
    RegraValidacao findByCategoria(String categoria);
}