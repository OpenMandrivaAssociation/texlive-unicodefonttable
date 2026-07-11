%global tl_name unicodefonttable
%global tl_revision 78793

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0k
Release:	%{tl_revision}.1
Summary:	A Unicode font table generator
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/unicodefonttable
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/unicodefonttable.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/unicodefonttable.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/unicodefonttable.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package produces font tables for unicode fonts as well as for 8bit
fonts. The table layout can be adjusted in various ways including
restricting the range of output to show only a portion of a specific
font. To quickly produce a one-off table there is a stand-alone version
unicodefont.tex that asks you a few questions and then generates the
table -- somewhat similar to nfssfont.tex for 8-bit fonts.

