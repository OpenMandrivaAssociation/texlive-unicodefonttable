Name:		texlive-unicodefonttable
Version:	71477
Release:	1
Summary:	A Unicode font table generator
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/unicodefonttable
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unicodefonttable.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unicodefonttable.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unicodefonttable.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package produces font tables for unicode fonts as well as
for 8bit fonts. The table layout can be adjusted in various
ways including restricting the range of output to show only a
portion of a specific font. To quickly produce a one-off table
there is a stand-alone version unicodefont.tex that asks you a
few questions and then generates the table --- somewhat similar
to nfssfont.tex for 8-bit fonts.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/unicodefonttable
%{_texmfdistdir}/tex/latex/unicodefonttable
%doc %{_texmfdistdir}/doc/latex/unicodefonttable

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
