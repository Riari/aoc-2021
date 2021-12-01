with import <nixpkgs> {};
let
  pythonEnv = python310.withPackages (p: [
    p.tabulate
  ]);
in mkShell {
  packages = [
    pythonEnv
  ];
}
