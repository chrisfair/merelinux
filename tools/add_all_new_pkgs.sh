#!/bin/sh
msg() {
    printf "%s\n" "$1"
}
error() {
    msg "ERROR: $1"
    exit 1
}
pkgdir="$1"
[ -d "$pkgdir" ] || error "Missing directory: ${pkgdir}"
pkgdir=$(realpath "$pkgdir")
name="merebuild-${pkgdir##*/}"
lxc-start -n $name -F -- /bin/env -i TERM=$TERM HOME=/tmp/wd /bin/sh -lc \
    'touch /merebuild/pkgs/buildlocal.db; \
     for file in $(find /tmp/staging -name "*.pkg*" | xargs) ; do \
        cp "$file" "/merebuild/pkgs/"; \
        repo-add -R "/merebuild/pkgs/buildlocal.db.tar.gz" "/merebuild/pkgs/${file##*/}"; \
     done'
lxc-destroy -n $name
