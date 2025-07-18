# 🐦 Polimorfismo com Herança em Python

Este projeto demonstra o conceito de **polimorfismo** utilizando **herança entre classes**, com exemplos práticos em Python.

---

## 📌 Conceitos abordados

- **Herança:** Classes filhas (`Pardal`, `Avestruz`, `Aviao`) herdando da classe base `Passaro`.
- **Polimorfismo:** A função `plano_de_voo()` aceita diferentes tipos de objetos que implementam o método `voar`, e cada um responde de maneira diferente.
- **Sobrescrita de métodos:** Cada classe filha sobrescreve o método `voar` da classe `Passaro`.

---

## 📄 Código de exemplo

```python
class Passaro:
    def voar(self):
        print("voando...")

class Pardal(Passaro):
    def voar(self):
        print("Pardal voa")

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")

class Aviao(Passaro):
    def voar(self):
        print("Avião decolando...")

def plano_de_voo(passaro):
    passaro.voar()

# Testando os objetos
plano_de_voo(Pardal())     # Pardal voa
plano_de_voo(Avestruz())   # Avestruz não voa
plano_de_voo(Aviao())      # Avião decolando...
