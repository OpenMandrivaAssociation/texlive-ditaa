Name:		texlive-ditaa
Version:	48932
Release:	1
Summary:	Use ditaa diagrams within LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ditaa
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ditaa.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ditaa.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
With this package ditaa (DIagrams Through Ascii Art) diagrams
can be embedded directly into LaTeX files.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/ditaa
%doc %{_texmfdistdir}/doc/latex/ditaa

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
