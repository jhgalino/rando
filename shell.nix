{ pkgs ? import <nixpkgs> {} }:
  let
    python = (
      (import (builtins.fetchTarball {
      url = "https://github.com/NixOS/nixpkgs/archive/eaeed9530c76ce5f1d2d8232e08bec5e26f18ec1.tar.gz";
      }) {}).python313
    );
    helix = (
         (import (builtins.fetchTarball {
            url = "https://github.com/NixOS/nixpkgs/archive/21808d22b1cda1898b71cf1a1beb524a97add2c4.tar.gz";
         }) {}).helix
       );
    basedpyright = (
         (import (builtins.fetchTarball {
            url = "https://github.com/NixOS/nixpkgs/archive/e73c3bf29132da092f9c819b97b6e214367eb71f.tar.gz";
         }) {}).basedpyright
       );
in
  pkgs.mkShell {
    buildInputs = [
      python
      helix
      basedpyright
     ];
     nativeBuildInputs = [
     ];
     shellHook = ''
         # blah blah blah
     '';
  }
