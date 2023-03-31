%global _python_bytecompile_build 0

Name:		texlive-texliveonfly
Version:	55777
Release:	2
Summary:	On-the-fly download of missing TeX live packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/texliveonfly
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texliveonfly.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texliveonfly.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-texliveonfly.bin = %{EVRD}

%description
The package provides a script that performs 'on the fly'
downloads of missing packages, while a document is being
compiled. (This feature is already available in the MikTeX
distribution for Windows machines.) To use the script, replace
your (LaTeX) compilation command with texliveonfly.py file.tex
(default options are --engine=lualatex and --arguments="-
synctex=1 -interaction=nonstopmode", both of which may be
changed). The script is designed to work on Linux
distributions.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/texliveonfly
%{_texmfdistdir}/scripts/texliveonfly/texliveonfly.py
%doc %{_texmfdistdir}/doc/support/texliveonfly/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/texliveonfly/texliveonfly.py texliveonfly
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
