{
  description = "python template";

  inputs = {
    devshell.url = "github:numtide/devshell";
    flake-utils.url = "github:numtide/flake-utils";
    # use https://lazamar.co.uk/nix-versions/ to search for older nixpkgs versions.
    # OR just scourge the git repo itself, if you're brave enough.
    # for example, this is nixpkgs from 2022-06-27:
    #nixpkgs.url = "https://github.com/NixOS/nixpkgs/archive/ff8b619cfecb98bb94ae49ca7ceca937923a75fa.tar.gz";
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, flake-utils, devshell, nixpkgs }:
    flake-utils.lib.eachDefaultSystem (system: {
      devShell =
        let pkgs = import nixpkgs {
          inherit system;
          config.allowUnfree = true; # sorry, Mr. Stallman
          overlays = [ devshell.overlays.default ];
        };

        in
        pkgs.devshell.mkShell {
          imports = [ (pkgs.devshell.importTOML ./devshell.toml) ];
          packages = [
            (pkgs.python312.withPackages(python-pkgs: [
              python-pkgs.requests
            ]))
          ];
        };
    });
}
