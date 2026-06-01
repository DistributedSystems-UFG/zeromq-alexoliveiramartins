[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wa7oHGos)

# ZeroMQ-Examples

Examples extracted from Tanenbaum&amp;vanSteen (2025) to illustrate three different communication patterns with ZeroMQ: client-server, pub-sub and producer-consumer.

---

## Producer Consumer pipeline

Máquina A: producer
PUSH bind tcp://\*:12345

Máquina B: extractor
PULL connect tcp://IP_MAQUINA_A:12345
PUSH connect tcp://IP_MAQUINA_C:8080

Máquina C: validator
PULL bind tcp://\*:8080
