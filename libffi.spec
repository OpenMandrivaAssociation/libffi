%define major 6
%define libname %mklibname ffi %{major}
%define devname %mklibname -d ffi
%define staticname %mklibname -d -s ffi

Summary:	A portable foreign function interface library
Name:		libffi
Version:	3.1
Release:	4
Group:		System/Libraries
License:	BSD
Url:		http://sourceware.org/%{name}
Source0:	ftp://sourceware.org/pub/%{name}/%{name}-%{version}.tar.gz
Patch0:		libffi-3.1-fix-include-path.patch
Patch1:		libffi-3.1-git-Fix-paths-in-libffi.pc.in.patch
BuildRequires:	autoconf

%track
prog %{name} = {
	url = http://sourceware.org/%{name}
	regex = "libffi-(__VER__)\.tar\.gz"
	version = %{version}
}

%description
Compilers for high level languages generate code that follow certain
conventions. These conventions are necessary, in part, for separate
compilation to work. One such convention is the "calling convention".
The calling convention is a set of assumptions made by the compiler
about where function arguments will be found on entry to a function. A
calling convention also specifies where the return value for a function
is found.

Some programs may not know at the time of compilation what arguments
are to be passed to a function.  For instance, an interpreter may be
told at run-time about the number and types of arguments used to call a
given function. `Libffi' can be used in such programs to provide a
bridge from the interpreter program to compiled code.

The `libffi' library provides a portable, high level programming
interface to various calling conventions. This allows a programmer to
call any function specified by a call interface description at run time.

FFI stands for Foreign Function Interface. A foreign function
interface is the popular name for the interface that allows code
written in one language to call code written in another language. The
`libffi' library really only provides the lowest, machine dependent
layer of a fully featured foreign function interface. A layer must
exist above `libffi' that handles type conversions for values passed
between the two languages.

%package -n	%{libname}
Summary:	A portable foreign function interface library
Group:		System/Libraries

%description -n	%{libname}
Compilers for high level languages generate code that follow certain
conventions. These conventions are necessary, in part, for separate
compilation to work. One such convention is the "calling convention".
The calling convention is a set of assumptions made by the compiler
about where function arguments will be found on entry to a function. A
calling convention also specifies where the return value for a function
is found.

Some programs may not know at the time of compilation what arguments
are to be passed to a function.  For instance, an interpreter may be
told at run-time about the number and types of arguments used to call a
given function. `Libffi' can be used in such programs to provide a
bridge from the interpreter program to compiled code.

The `libffi' library provides a portable, high level programming
interface to various calling conventions. This allows a programmer to
call any function specified by a call interface description at run time.

FFI stands for Foreign Function Interface. A foreign function
interface is the popular name for the interface that allows code
written in one language to call code written in another language. The
`libffi' library really only provides the lowest, machine dependent
layer of a fully featured foreign function interface. A layer must
exist above `libffi' that handles type conversions for values passed
between the two languages.


%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	ffi-devel = %{EVRD}
Obsoletes:	%{mklibname -d ffi 5} < %{EVRD}

%description -n %{devname}
This package contains libraries and header files for developing
applications that use %{name}.


# The static libffi is used to link Host Dalvik while building
# Android from source - please don't remove it.
%package -n	%{staticname}
Summary:	Static libraries for %{name}
Group:		Development/C
Requires:	%{devname} = %{EVRD}
Provides:	ffi-static-devel = %{EVRD}

%description -n %{staticname}
This package contains static libraries for developing
applications that use %{name}.

%prep
%setup -q
%apply_patches
autoreconf -fiv

%build
%ifarch %arm aarch64
export CC=gcc
%endif
%configure --enable-static
%make

%install
%makeinstall_std
%multiarch_includes %{buildroot}%{_includedir}/ffi.h

%files -n %{libname}
%{_libdir}/libffi.so.%{major}*

%files -n %{devname}
%doc LICENSE README
%{_libdir}/pkgconfig/libffi.pc
%{_includedir}/ffi*.h
%{multiarch_includedir}/ffi.h
%{_libdir}/libffi.so
%{_mandir}/man3/*
%{_infodir}/libffi.info.*

%files -n %{staticname}
%{_libdir}/*.a
