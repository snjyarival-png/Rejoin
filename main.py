#!/usr/bin/env python3

import os

# Variabel konfigurasi
package = ""
link = ""
delay = "3"
interval = "2"
retry = "5"

def clear():
    os.system("clear")

def banner():
    clear()
    print("╔══════════════════════════════╗")
    print("║      ROBLOX REJOIN V2        ║")
    print("╚══════════════════════════════╝")
    print("RIFT\n")

while True:
    banner()

    print("[1] Mulai Monitor")
    print("[2] Pilih Package")
    print("[3] Ubah Link")
    print("[4] Pengaturan")
    print("[5] Lihat Log")
    print("[6] Keluar")
    print()

    pilih = input("Pilih Menu : ")

    if pilih == "1":
        clear()
        print("=== MULAI MONITOR ===\n")

        if package == "":
            print("Package belum dipilih.")
        elif link == "":
            print("Link belum diisi.")
        else:
            print("Konfigurasi")
            print("-----------------------")
            print("Package :", package)
            print("Link    :", link)
            print("Delay   :", delay)
            print("Interval:", interval)
            print("Retry   :", retry)
            print("\nMonitor belum diimplementasikan.")

        input("\nTekan ENTER untuk kembali...")

    elif pilih == "2":
        clear()
        print("=== PILIH PACKAGE ===\n")

        result = os.popen("pm list packages | grep roblox").read().splitlines()

        if not result:
            print("Tidak ditemukan package Roblox.\n")
            package = input("Masukkan package manual : ")

        else:
            packages = []

            for i, p in enumerate(result, 1):
                p = p.replace("package:", "")
                packages.append(p)
                print(f"[{i}] {p}")

            print(f"[{len(packages)+1}] Manual")

            pilih_pkg = input("\nPilih : ")

            if pilih_pkg.isdigit():

                pilih_pkg = int(pilih_pkg)

                if 1 <= pilih_pkg <= len(packages):
                    package = packages[pilih_pkg-1]

                elif pilih_pkg == len(packages)+1:
                    package = input("Masukkan package : ")

        print("\nPackage dipilih :", package)
        input("\nTekan ENTER...")

    elif pilih == "3":
        clear()
        print("=== UBAH LINK ===\n")

        link = input("Masukkan Link : ")

        print("\nLink berhasil disimpan.")
        input("\nTekan ENTER...")

    elif pilih == "4":
        clear()
        print("=== PENGATURAN ===\n")

        delay = input(f"Delay ({delay}) : ") or delay
        interval = input(f"Interval ({interval}) : ") or interval
        retry = input(f"Retry ({retry}) : ") or retry

        print("\nPengaturan disimpan.")
        input("\nTekan ENTER...")

    elif pilih == "5":
        clear()
        print("=== LOG ===\n")
        print("Belum ada log.")
        input("\nTekan ENTER...")

    elif pilih == "6":
        print("\nTerima kasih.")
        break

    else:
        input("\nMenu tidak tersedia. Tekan ENTER...")
