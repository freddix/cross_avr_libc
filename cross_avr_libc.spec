Summary:	C runtime library for the AVR
Name:		cross_avr_libc
Version:	1.8.0
Release:	3
License:	Modified BSD (see included LICENSE)
Group:		Development/Tools
Source0:	http://download.savannah.gnu.org/releases/avr-libc/avr-libc-%{version}.tar.bz2
# Source0-md5:	54c71798f24c96bab206be098062344f
BuildRequires:	cross_avr_gcc
Requires:	cross_avr_gcc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		target		avr
%define		arch		%{_prefix}/%{target}

%define		__strip		%{target}-strip

%description
Contains the standard C library for Atmel AVR microcontrollers.

%prep
%setup -qn avr-libc-%{version}

%build
CFLAGS="%{rpmcflags}" \
CXXFLAGS="%{rpmcflags}" \
./configure \
	--prefix=%{_prefix} \
	--build=%{_target_platform} \
	--host=%{target}
%{__make} \
	DOC_INST_DIR="%{_datadir}/%{name}-%{version}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if 0%{!?debug:1}
%{target}-strip -g $RPM_BUILD_ROOT%{arch}/lib/*.[oa] \
	$RPM_BUILD_ROOT%{arch}/lib/avr?/*.[oa]
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README NEWS
%attr(755,root,root) %{_bindir}/*
%dir %{arch}/include
%dir %{arch}/include/avr
%dir %{arch}/include/compat
%dir %{arch}/include/util
%dir %{arch}/lib/avr*
%{arch}/include/*.h
%{arch}/include/avr/*.h
%{arch}/include/compat/*.h
%{arch}/include/util/*.h
%{arch}/lib/*.[oa]
%{arch}/lib/avr*/*.[oa]

