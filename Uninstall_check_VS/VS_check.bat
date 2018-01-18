rem check component path 
"C:\Program Files (x86)\Microsoft Visual Studio\Installer\vswhere.exe" -version [15.0,16.0) -property installationPath

 

"C:\Program Files (x86)\Microsoft Visual Studio\Installer\vswhere.exe" -products Microsoft.VisualStudio.Product.Enterprise -version [15.0,16.0)  -requires Microsoft.VisualStudio.VC.Ide.Core -property installationPath

 

"C:\Program Files (x86)\Microsoft Visual Studio\Installer\vswhere.exe" -products Microsoft.VisualStudio.Product.Enterprise -version [15.0,16.0) -requires Microsoft.VisualStudio.VC.MSBuild.Base -property installationPath

 

"C:\Program Files (x86)\Microsoft Visual Studio\Installer\vswhere.exe" -products Microsoft.VisualStudio.Product.Enterprise -version [15.0,16.0) -requires Microsoft.VisualStudio.Component.CoreEditor -property installationPath

 

"C:\Program Files (x86)\Microsoft Visual Studio\Installer\vswhere.exe" -products Microsoft.VisualStudio.Product.Enterprise -version [15.0,16.0) -requires Microsoft.VisualStudio.ComponentGroup.NativeDesktop.Core -property installationPath
