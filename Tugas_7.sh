#!/bin/bash

Luas_bidang_Persegi() {
  panjang=$p
  lebar=$l
  echo "$panjang"
  echo "$lebar"
}

echo "Masukkan Panjang :"
read panjang
echo "Masukkan Lebar :"
read lebar
let luas=$panjang*$lebar
echo -e "Luas Persegi : \n$luas "

printf "\n"
Luas_bidang_Persegi $panjang $lebar
