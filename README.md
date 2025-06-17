# Script de Escaneo de OLTs en SecureCRT

Este script permite escanear el estado de 64 ONUs de un slot específico en equipos OLT usando SecureCRT.

## Funcionalidades

- Selección de slot mediante una interfaz gráfica
- Ejecución automática del comando "onu show" para visualizar todo el slot completo
- Ejecución automática del comando "onu status" para cada OLT individual
- Formato de slot compatible (ejemplo: 1-1, 2-3, etc.)
- Soporte para múltiples slots (1-1 hasta 7-8)

## Requisitos

- SecureCRT instalado
- Conexión establecida a un equipo OLT

## Instrucciones de uso

1. Abrir SecureCRT y conectarse al equipo OLT
2. Cargar el script desde el menú de scripts
3. Ingresar el número de slot en el formato solicitado (ej: 1-1)
4. Esperar a que el script complete el escaneo
   - Primero ejecutará "onu show" para visualizar el slot completo
   - Luego ejecutará "onu status" para cada una de las 64 ONUs

## Notas

El script ejecuta comandos en serie y puede tomar tiempo dependiendo de la respuesta del equipo.
