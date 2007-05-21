Summary: Utilities for working with LUKS-protected filesystems
Name: luks-tools
Version: 0.0.11
Release: %mkrel 1
License: GPL
Group: File tools
Source: http://www.flyn.org/projects/%name/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
URL: http://www.flyn.org
Requires: cryptsetup-luks
BuildRequires: cryptsetup-luks

%description
The luks-tools package contains various utilities for working with 
LUKS-protected filesystems. HAL uses these utilites to automatically 
mount encrypted volumes when they are attached to a system, provided 
the user can produce the correct passphrase. These utilities are 
written as separate programs to allow MAC systems like SELinux to 
have fine-grained control over them.

luks-format
    A utility that formats a filesystem to contain a LUKS encryption 
    header.

luks-is-encrypted
    A tool that can determine if a filesystem contains a LUKS 
    encryption header.

luks-setup
    A utility that sets up the dm-crypt device map for a partition.

gnome-luks-format
    A GNOME front-end for luks-format.



%prep
%setup -q

%build
PATH="$PATH:/sbin" %configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README FAQ
%{_datadir}/luks-tools/*
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man*/*
