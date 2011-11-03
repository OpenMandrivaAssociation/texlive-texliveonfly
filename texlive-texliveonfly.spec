# revision 24200
# category Package
# catalog-ctan /support/texliveonfly
# catalog-date 2011-10-04 11:31:57 +0200
# catalog-license gpl3
# catalog-version undef
Name:		texlive-texliveonfly
Version:	20111004
Release:	1
Summary:	On-the-fly download of missing TeX live packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/texliveonfly
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texliveonfly.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texliveonfly.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Provides:	texlive-texliveonfly.bin = %{EVRD}
Conflicts:	texlive-texmf <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/texliveonfly
%{_texmfdistdir}/scripts/texliveonfly/texliveonfly.py
%doc %{_texmfdistdir}/doc/support/texliveonfly/README
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/texliveonfly/texliveonfly.py texliveonfly
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}