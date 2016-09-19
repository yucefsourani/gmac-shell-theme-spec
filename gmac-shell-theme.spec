%global debug_package %{nil}
Name:           gmac-shell-theme
Version:        1
Release:        1%{?dist}
Summary:        Gmac Gnome Shell Theme
Group:		      User Interface/Desktops
License:        GPLv3
URL:            https://sourceforge.net/projects/gmaclinux/
Source0:        https://github.com/yucefsourani/gmac-shell-theme/raw/master/archives/Gmac-Shell-1.tar.bz2
BuildArch:	    noarch
Requires:	      filesystem


%description
Gmac Gnome Shell Theme

%prep
%autosetup -n Gmac-Shell


%build



%install
rm -rf $RPM_BUILD_ROOT
%{__mkdir} -p %{buildroot}%{_datadir}/themes/%{name}
%{__cp} -rf * %{buildroot}%{_datadir}/themes/%{name}


%files
%license COPYING
%doc AUTHOR
%{_datadir}/themes/%{name}


%changelog
* Mon Sep 19 2016 youcef sourani youssef.m.sourani@gmail.com - 1-1
- Initial for Fedora
