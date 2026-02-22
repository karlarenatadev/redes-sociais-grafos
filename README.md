# 📊 Análise de Engajamento no Instagram com Grafos (Neo4j)

## 📌 Visão Geral

Este projeto tem como objetivo analisar padrões de engajamento em postagens do Instagram utilizando modelagem em grafos com Neo4j.

A partir de um dataset real, foram modeladas entidades como **Posts**, **Categorias** e **Tipos de Mídia**, permitindo explorar relações e identificar padrões de desempenho.

---

## 🎯 Objetivos

* Modelar dados de redes sociais em formato de grafo
* Analisar o engajamento por:

  * Tipo de mídia (image, carousel, reel)
  * Categoria de conteúdo (fashion, fitness, food, etc.)
* Identificar padrões de performance e variabilidade
* Explorar trade-offs entre **consistência e potencial de engajamento**

---

## 🧱 Modelagem do Grafo

### Nós:

* `Post`

  * id
  * likes
  * comments
  * engagement

* `Category`

  * name

* `MediaType`

  * type (image, carousel, reel)

---

### Relacionamentos:

* `(Post)-[:HAS_CATEGORY]->(Category)`
* `(Post)-[:HAS_MEDIA]->(MediaType)`

---

## ⚙️ Tecnologias Utilizadas

* Neo4j Aura (banco de dados em grafo)
* Cypher (linguagem de consulta)
* Python (exploração inicial dos dados)
* Dataset público do Kaggle

---

## 📥 Importação de Dados

```cypher
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/karlarenatadev/redes-sociais-grafos/refs/heads/main/instagram.csv' AS row
CREATE (p:Post {
  id: row.post_id,
  likes: toInteger(row.likes),
  comments: toInteger(row.comments),
  engagement: toFloat(row.engagement_rate)
})
```

---

## 📊 Análises Realizadas

### 🔹 Engajamento médio por tipo de mídia

* Diferenças pequenas entre image, carousel e reel
* Indicação de que o formato isolado não é determinante

### 🔹 Engajamento por categoria + tipo

* Algumas combinações apresentam desempenho levemente superior
* Exemplo:

  * Fashion + Reel → maior média
  * Food + Image → desempenho consistente

### 🔹 Média vs Desvio Padrão

* Alto desvio em relação à média
* Indica grande variabilidade no desempenho

---

## 🧠 Principais Insights

* Não existe um formato universalmente melhor
* O engajamento apresenta alta variabilidade
* Estratégias podem ser classificadas como:

  * 🔥 Alta média + alto desvio → alto risco / alto potencial
  * 🧠 Média estável → previsibilidade
* Fatores externos (criatividade, timing, conteúdo) provavelmente têm grande impacto

---

## 🚀 Possíveis Melhorias

* Criar sistema de recomendação baseado em score:

  ```
  score = média - peso * desvio
  ```

* Adicionar análise temporal

* Incluir dados de usuários (creator vs brand)

* Visualização interativa do grafo

---

## 📎 Conclusão

Este projeto demonstra como grafos podem ser utilizados para analisar dados de redes sociais, indo além de médias simples e explorando a variabilidade dos dados.

Mais do que identificar "o melhor formato", o projeto evidencia a importância de interpretar incerteza e contexto na tomada de decisão.

---

