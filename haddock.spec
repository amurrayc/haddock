# This is an RPM spec file that specifies how to package
# haddock for Red Hat Linux and, possibly, similar systems.
# It has been tested on Red Hat Linux 7.2.
#
# If this file is part of a tarball, you can build RPMs directly from
# the tarball by using the following command:
#
#    rpm -ta haddock-(VERSION)-src.tar.gz
#
# The resulting package will be placed in the RPMS/(arch) subdirectory
# of your RPM build directory (usually /usr/src/redhat or ~/rpm), with
# the name haddock-(VERSION)-(RELEASE).noarch.rpm.  A corresponding
# source RPM package will be in the SRPMS subdirectory.
#
# NOTE TO HADDOCK MAINTAINERS: When you release a new version of
# Haskell mode, update the version definition below to match the
# version label of your release tarball.

%define name haddock
%define version 0.4
%define release 1

Summary: Haddock documentation tool for annotated Haskell source code
Name: %{name}
Version: %{version}
Release: %{release}
License: BSD-like
Group: Development/Tools
Source: http://www.haskell.org/haddock/haddock-%{version}-src.tar.gz
URL: http://www.haskell.org/haddock/
Packager: Tom Moertel <tom-rpms@moertel.com>
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Prefix: %{_prefix}
#BuildRequires: ghc

%description
Haddock is a tool for automatically generating documentation from
annotated Haskell source code. It is primary intended for documenting
libraries, but it should be useful for any kind of Haskell code.

Haddock lets you write documentation annotations next to the
definitions of functions and types in the source code, in a syntax
that is easy on the eye when writing the source code (no heavyweight
mark-up). The documentation generated by Haddock is fully hyperlinked
-- click on a type name in a type signature to go straight to the
definition, and documentation, for that type.

Haddock can generate documentation in multiple formats; currently HTML
is implemented, and there is partial support for generating DocBook.
The generated HTML uses stylesheets, so you need a fairly up-to-date
browser to view it properly (Mozilla, Konqueror, Opera, and IE 6
should all be ok).

%prep
%setup -n haddock-%{version}

%build
./configure --prefix=%{prefix}
make
(cd haddock/doc ; make dvi ps html ; gzip -f -9 *.dvi *.ps )

%install
rm -rf ${RPM_BUILD_ROOT}
make prefix=${RPM_BUILD_ROOT}%{prefix} install

%clean
rm -rf ${RPM_BUILD_ROOT}
# rm -rf ${RPM_BUILD_DIR}/haddock-%{version}

%files
%defattr(-,root,root)
%doc haddock/README
%doc haddock/doc/haddock
%doc haddock/doc/haddock.dvi.gz
%doc haddock/doc/haddock.ps.gz
%{prefix}/lib/haddock-%{version}
%{prefix}/bin/haddock
%{prefix}/bin/haddock-%{version}

%changelog

* Wed May 01 2002 Tom Moertel <tom-rpms@moertel.com>
- Created spec file
* Sun Jun 23 2002 Sven Panne <sven_panne@yahoo.com>
- Cleaned up build root handling and added more docs
