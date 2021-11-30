{ pkgs ? import <nixpkgs> {} }:
let
    aoc-2021 = pkgs.python3.withPackages (p: with p; []);
in
aoc-2021.env 