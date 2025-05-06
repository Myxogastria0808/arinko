{
  description = "dashi-server flake";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    rust-overlay.url = "github:oxalica/rust-overlay";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      nixpkgs,
      rust-overlay,
      flake-utils,
      ...
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        overlays = [ (import rust-overlay) ];
        pkgs = import nixpkgs {
          inherit system overlays;
        };
      in
      {
        devShells.default =
          with pkgs;
          mkShell {
            buildInputs = [
              bacon
              # build target: https://ryochack.hatenablog.com/entry/2017/10/22/014735
              (rust-bin.stable.latest.default.override { extensions = [ "rust-src" ]; targets = [ "x86_64-unknown-linux-gnu" "86_64-pc-windows-msvc" ] })
              sea-orm-cli
            ];
            RUST_SRC_PATH = "${pkgs.rust.packages.stable.rustPlatform.rustLibSrc}";
          };
      }
    );
}