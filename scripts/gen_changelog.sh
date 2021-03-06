#!/bin/bash -e
error() {
    printf 'ERROR: %s\n' "$1"
    exit 1
}

pkgdir="$1"
[ -d "$pkgdir" ] || error "Missing directory: ${pkgdir}"
shift
comment=$*
[ -z "$comment" ] && comment='Initial version'

# shellcheck disable=SC1090
. "${pkgdir}/PKGBUILD"

[ -n "$changelog" ] || changelog='ChangeLog'

[ -n "$MERE_PACKAGER" ] ||
    MERE_PACKAGER=$(grep '^#.*Maintainer:' "${pkgdir}/PKGBUILD" | \
                    sed 's/.*://')

file=$(mktemp)
printf 'Added the following to the top of %s:\n\n' "$changelog"

# shellcheck disable=SC2154
printf '%s %s\n\n\t* %s-%s :\n\t%s\n\n' "$(date +%Y-%m-%d)" "$MERE_PACKAGER" \
    "$pkgver" "$pkgrel" "$comment" | tee "$file"

[ -f "${pkgdir}/${changelog}" ] && cat "${pkgdir}/${changelog}" >>"$file"
mv "$file" "${pkgdir}/${changelog}"
