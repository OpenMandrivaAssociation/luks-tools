Summary: Utilities for working with LUKS-protected filesystems
Name: luks-tools
Version: 0.0.12
Release: %mkrel 1
License: GPL
Group: File tools
Source0: http://www.flyn.org/projects/%name/%{name}-%{version}.tar.bz2
# (fc) 0.0.12-1mdv fix pam-stack deprecated usage
Patch0: luks-tools-0.0.12-fixpamstack.patch
# (fc) 0.0.12-1mdv fix consolehelper file
Patch1: luks-tools-0.0.12-fixconsolehelper.patch
URL: http://www.flyn.org
Requires: cryptsetup-luks
Requires: usermode
BuildRequires: cryptsetup-luks
BuildRequires: glib2-devel
BuildRequires: libext2fs-devel

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
%patch0 -p1 -b .fixpamstack
%patch1 -p1 -b .fixconsolehelper

%build
PATH="$PATH:/sbin" %configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

mv $RPM_BUILD_ROOT%{_bindir}/gnome-luks-format $RPM_BUILD_ROOT%{_sbindir}/gnome-luks-format 
ln -s consolehelper $RPM_BUILD_ROOT%{_bindir}/gnome-luks-format 

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README FAQ
%{_sysconfdir}/pam.d/*
%{_sysconfdir}/security/console.apps/*
%{_datadir}/luks-tools/*
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man*/*
