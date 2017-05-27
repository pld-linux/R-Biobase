%define		packname	Biobase

Summary:	Base functions for Bioconductor
Name:		R-%{packname}
Version:	2.22.0
Release:	3
License:	Artistic 2.0
Group:		Applications/Science
Source0:	http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	97b4dd96418b87b47d62c955d54924b7
URL:		http://bioconductor.org/packages/release/bioc/html/Biobase.html
BuildRequires:	R
BuildRequires:	R-BiocGenerics >= 0.3.2
BuildRequires:	texlive-latex
Requires:	R
Requires:	R-BiocGenerics >= 0.3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Base functions for Bioconductor (bioconductor.org). Biobase provides
functions that are needed by many other Bioconductor packages or which
replace R functions.

%prep
%setup -c -q -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/Meta/
%{_libdir}/R/library/%{packname}/R/
%{_libdir}/R/library/%{packname}/help/
%{_libdir}/R/library/%{packname}/libs/
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/data
%{_libdir}/R/library/%{packname}/scripts
%{_libdir}/R/library/%{packname}/ExpressionSet
%{_libdir}/R/library/%{packname}/CITATION
%{_libdir}/R/library/%{packname}/Code
%{_libdir}/R/library/%{packname}/extdata
%{_libdir}/R/library/%{packname}/testClass.R
%{_libdir}/R/library/%{packname}/NEWS
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/html
