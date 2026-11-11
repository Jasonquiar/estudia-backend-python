# Encuentro 1 · Reglas de un servicio

**Pregunta del día:** ¿qué debe impedir un servicio backend, y cómo demostramos que lo impide?

| Archivo | Qué es |
|---|---|
| `diagnostico.py` | Calentamiento: predice la salida antes de ejecutar |
| `inventario_v1.py` | Un inventario que registra salidas… ¿qué podría salir mal? |
| `inventario_v2.py` | Una entidad con una operación que **rechaza** un cambio inválido |
| `reservas_practica.py` | Práctica: completa `reservar()` |

```bash
python3 diagnostico.py
python3 inventario_v1.py
python3 inventario_v2.py
python3 reservas_practica.py
```

## Práctica: reservas de una sala de ensayo

Sala de ensayo de una casa de la cultura. Ya hay una reserva de **18 a 19**. Llegan dos solicitudes: **A)** 19 a 20 · **B)** 18 a 20.

1. Para A y B escribe: **entrada · resultado esperado (acepta/rechaza) · motivo**.
2. Completa los `TODO` de `reservar()` en `reservas_practica.py`.
3. **Antes de ejecutar**, escribe qué esperas que imprima. Ejecuta y compara.

**Reto:** agrega el caso C) 21 a 20. ¿Se rechaza por una regla de negocio o por un dato inválido? ¿Por qué 19–20 **no** choca con 18–19?

## Para tu proyecto

En la ficha de tu proyecto, deja escritas:
- 2 necesidades (qué hay que registrar, consultar o modificar, y quién lo usa),
- 1 regla de negocio (algo que el servicio nunca debe permitir o siempre debe cumplir),
- 1 caso que se acepta y 1 caso que se rechaza.

**Para pensar antes del próximo encuentro:** ¿tu regla vive mejor en una función o en un método de una clase? Trae una razón.
