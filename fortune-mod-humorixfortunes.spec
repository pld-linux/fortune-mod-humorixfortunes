Summary:	Collection of Humorix Fortunes
Summary(pl.UTF-8):   Kolekcja fortunek z Humoriksa
Name:		fortune-mod-humorixfortunes
Version:	1.4
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://humorix.org/downloads/humorixfortunes-%{version}.tar.gz
# Source0-md5:	a0f5eb298aa5982aa54571f6e46aa58b
URL:		http://humorix.org/downloads/#Fortunes
Requires:	fortune-mod
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
They include: 
- Linux slogans and one-liners.
- Quotes froms Linus Torvalds and others.
- Brief Microsoft jokes, stories, and one-liners.
- Condensed Humorix articles.

%description -l pl.UTF-8
Zawierają:
- Linuksowe slogany i jednolinijkowe cytaty.
- Cytaty z Linusa Tovaldsa i innych.
- Krótkie dowcipy, opowiadania i jednolinijkowe cytaty o Microsofcie.
- Skondensowane artykuły Humoriksa.

%prep
%setup -q -n humorixfortunes-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/games/fortunes

install humorix* $RPM_BUILD_ROOT%{_datadir}/games/fortunes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/games/fortunes/*
