%global tl_name ditaa
%global tl_revision 48932

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.9
Release:	%{tl_revision}.1
Summary:	Use ditaa diagrams within LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ditaa
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ditaa.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ditaa.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
With this package ditaa (DIagrams Through Ascii Art) diagrams can be
embedded directly into LaTeX files.

