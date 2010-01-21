Name: x11-font-misc-meltho
Version: 1.0.1
Release: %mkrel 1
Summary: Xorg X11 font misc-meltho
Group: Development/X11
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/font/font-misc-meltho-%{version}.tar.bz2
# We may not modify the software!
License: Meltho Font License
BuildArch: noarch
BuildRequires: x11-font-util >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: fontconfig 
Requires(post): mkfontdir
Requires(postun): mkfontdir
Requires(post): mkfontscale
Requires(postun): mkfontscale

%description
Xorg X11 font misc-meltho

%prep
%setup -q -n font-misc-meltho-%{version}

%build
./configure --prefix=/usr --x-includes=%{_includedir}\
	    --x-libraries=%{_libdir} --with-fontdir=%_datadir/fonts/OTF

%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%_datadir/fonts/OTF/fonts.dir
rm -f %{buildroot}%_datadir/fonts/OTF/fonts.scale

%post
mkfontscale %_datadir/fonts/OTF
mkfontdir %_datadir/fonts/OTF

%postun
mkfontscale %_datadir/fonts/OTF
mkfontdir %_datadir/fonts/OTF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%_datadir/fonts/OTF/SyrCOM*.otf
