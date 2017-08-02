%global realname jiffy
%global commit 1febce3ca86c5ca5d5a3618ed3d5f125bb99e4c5

Name:           erlang-%{realname}
Version:        0.14.8
Release:        %mkrel 2
Summary:        Erlang JSON parser
Group:          Development/Erlang
License:        MIT
URL:            https://github.com/davisp/jiffy
Source0:        https://github.com/davisp/jiffy/archive/%{commit}/%{realname}-%{commit}.tar.gz
Patch1:         jiffy-system-double-conversion.patch

BuildRequires:  erlang >= R14B
BuildRequires:  erlang-rebar
BuildRequires:  gcc-c++
BuildRequires:  double-conversion-devel

#%{?__erlang_nif_version:Requires: %{__erlang_nif_version}}

Provides:       %{realname} = %{version}
Obsoletes:      %{realname} < %{version}

%description
A JSON parser for Erlang implemented as a NIF.


%prep
%setup -q -n %{realname}-%{commit}
%patch1 -p1 -b .system-double-conversion
rm -r c_src/double-conversion


%build
%{erlang_compile}


%install
%{erlang_install}


%check
%{erlang_test}


%files
%{erlang_appdir}/
%doc README.md
%license LICENSE



%changelog
* Fri May 06 2016 neoclust <neoclust> 0.14.8-2.mga6
+ Revision: 1009839
- imported package erlang-jiffy

