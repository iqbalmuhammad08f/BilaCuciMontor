-- Active: 1745938775538@@127.0.0.1@5432@bila_cuci_montor@public
CREATE TABLE users (
    id_user SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    role VARCHAR(20) NOT NULL,
    status BOOLEAN NOT NULL DEFAULT true
);

CREATE TABLE admins (
    id_admin SERIAL PRIMARY KEY,
    nama VARCHAR(50) NOT NULL,
    email VARCHAR(50),
    nomor_hp VARCHAR(20),
    status BOOLEAN NOT NULL DEFAULT true,
    id_user INT REFERENCES users(id_user) NOT NULL
);

CREATE TABLE karyawan (
    id_karyawan SERIAL PRIMARY KEY,
    nama VARCHAR(50) NOT NULL,
    email VARCHAR(50),
    nomor_hp VARCHAR(20),
    alamat TEXT,
    role VARCHAR(20) NOT NULL,
    tanggal_masuk DATE NOT NULL DEFAULT now(),
    status BOOLEAN NOT NULL DEFAULT true
);

CREATE TABLE members (
    id_member SERIAL PRIMARY KEY,
    nama VARCHAR(50) NOT NULL,
    email VARCHAR(50),
    nomor_hp VARCHAR(20),
    alamat TEXT,
    tanggal_daftar DATE NOT NULL DEFAULT now(),
    tanggal_berakhir DATE,
    status BOOLEAN NOT NULL DEFAULT false,
    id_user INT REFERENCES users(id_user) NOT NULL
);

CREATE TABLE paket_member (
    id_paket SERIAL PRIMARY KEY,
    nama VARCHAR(50) NOT NULL,
    harga INT NOT NULL,
    durasi INT NOT NULL, 
    status BOOLEAN NOT NULL DEFAULT true
);

CREATE TABLE pembayaran_member (
    id_pembayaran SERIAL PRIMARY KEY,
    id_member INT REFERENCES members(id_member) NOT NULL,
    id_paket INT REFERENCES paket_member(id_paket) NOT NULL,
    tanggal TIMESTAMP NOT NULL DEFAULT NOW(),
    total INT NOT NULL
);

CREATE TABLE metode_pembayaran (
    id_metode SERIAL PRIMARY KEY,
    nama_metode VARCHAR(50) NOT NULL,
    status BOOLEAN NOT NULL
);

CREATE TABLE transaksi (
    id_transaksi SERIAL PRIMARY KEY,
    id_member INT REFERENCES members(id_member),
    id_karyawan INT REFERENCES karyawan(id_karyawan) NOT NULL,
    id_metode INT REFERENCES metode_pembayaran(id_metode),
    tanggal DATE NOT NULL DEFAULT NOW(),
    uang INT,
    total INT
);

CREATE TABLE layanan (
    id_layanan SERIAL PRIMARY KEY,
    nama_layanan VARCHAR(50) NOT NULL,
    harga INT NOT NULL,
    status BOOLEAN NOT NULL DEFAULT true
);

CREATE TABLE detail_transaksi (
    id_detail SERIAL PRIMARY KEY,
    id_transaksi INT REFERENCES transaksi(id_transaksi) NOT NULL,
    id_layanan INT REFERENCES layanan(id_layanan) NOT NULL,
    plat VARCHAR(15) NOT NULL,
    nama_kendaraan VARCHAR(50) NOT NULL,
    subtotal INT
);
