%global tl_name texliveonfly
%global tl_revision 76924
%global tl_bin_links texliveonfly:%{_texmfdistdir}/scripts/texliveonfly/texliveonfly.py

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	On-the-fly download of missing TeX Live packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/texliveonfly
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texliveonfly.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texliveonfly.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(texliveonfly.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
The package provides a script that performs 'on the fly' downloads of
missing packages, while a document is being compiled. (This feature is
already available in the MiKTeX distribution for Windows machines.) To
use the script, replace your (LaTeX) compilation command with
texliveonfly.py file.tex (default options are --engine=pdflatex and
--arguments="-synctex=1 -interaction=nonstopmode", which may all be
changed). The script is designed to work on Linux distributions.

