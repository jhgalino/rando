{ pkgs ? import <nixpkgs> {} }:
  let
    python = (
      (import (builtins.fetchTarball {
      url = "https://github.com/NixOS/nixpkgs/archive/eaeed9530c76ce5f1d2d8232e08bec5e26f18ec1.tar.gz";
      }) {}).python313
    );
in
  pkgs.mkShell {
    buildInputs = [
      python
     ];
     nativeBuildInputs = [
     ];
     shellHook = ''
         # blah blah blah
     '';
  }
