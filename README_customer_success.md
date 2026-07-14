# Customer Success Overview PowerPoint Generator

Este repositorio contiene scripts y recursos para generar presentaciones PowerPoint con mockups.

## Rama: customer-success-mockup-ppt

Esta rama contiene el generador de PowerPoint para el mockup del Customer Success Overview.

## Contenido

- `presentations/Customer_Success_Overview_Mockup.py` - Script Python para generar el PowerPoint
- `images/` - Carpeta para las imágenes de mockups

## Requisitos

- Python 3.6 o superior
- python-pptx

## Instalación

```bash
pip install python-pptx
```

## Uso

1. Asegúrate de tener la imagen del mockup (`V4_3.3.1.1_Customer_Success_Overview_Importe_menu.png`) en el directorio del script
2. Ejecuta el script:

```bash
python presentations/Customer_Success_Overview_Mockup.py
```

3. El archivo `Customer_Success_Overview_Mockup.pptx` se generará en el directorio actual

## Descripción del Mockup

El mockup muestra el Overview de Customer Success de ClickEdu con las siguientes secciones:
- Total a renovar: 10,9 M€ (26%)
- Renovado: 4,6 M€ | 42,0%
- Por renovar: 5,7 M€ | 52,5%
- Bajas: 0,6 M€ | 5,5%
- Ventas adición vs ppto: 1,8 M€ | +5,5%

Incluye gráficos por:
- Comunidad Autónoma
- Segmento (Privados, Concertados, Público)
- Tier (Tier 1, Tier 2, Tier 3)
- Evolutivo acumulado importe renovado

## Notas

- El PowerPoint generado tiene formato 16:9
- La imagen del mockup ocupa toda la diapositiva
- Puedes personalizar el script para añadir más diapositivas o modificar el diseño
