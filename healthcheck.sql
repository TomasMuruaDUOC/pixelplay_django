-- healthcheck.sql
-- Script para verificar que la base de datos Oracle está funcionando correctamente
-- Usado por Docker para healthcheck

WHENEVER SQLERROR EXIT FAILURE
SELECT 1 FROM DUAL;
EXIT