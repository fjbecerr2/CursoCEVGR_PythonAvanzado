-- Crear la Base de Datos
CREATE DATABASE DBBiblioTester;
COMMIT;

-- Crear el Usuario
GRANT ALL ON DBBiblioTester.* TO 'bibliotecario'@'localhost' IDENTIFIED BY 'biblioteca';
COMMIT;
USE DBBiblioTester;
COMMIT;

-- Crear la  tabla
CREATE TABLE BIBLIOTECA_TESTER (id INT, Tematica VARCHAR(50), Titulo VARCHAR(50),Formato VARCHAR(50), Paginas INT, Puntuacion INT);
COMMIT;