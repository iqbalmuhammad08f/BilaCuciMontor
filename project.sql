-- Active: 1745938775538@@127.0.0.1@5432@projectbasda@public
CREATE Table penghuni_kos(
  id_penghuni SERIAL PRIMARY KEY,
  nama VARCHAR(100) NOT NULL,
  umur NUMERIC
)