# TODO:
# Check: %description -l pl
#   - what does it mean: one-liners

Summary:	Collection of Humorix Fortunes
Summary(pl):	Kolekcja fortunek z Humorixa
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

%description -l pl
Zawieraj±:
- Linuksowe slogany i krótkie cytaty.
- Cytaty Linusa Tovaldsa i innych.
- Dowcipy o Microsofcie, opowiadania i krótkie cytaty.
- Skondensowane artyku³y Humorixa.


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
