function Instalar-PythonMaisRecente() {
    Write-Host "Install the latest version of Python..."
    
    # Defina o URL para o instalador Python (mais recente)
    $pythonInstallerUrl = "https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe"

    # Set the URL for the Python installer (latest)
    $pythonInstallerPath = "$env:USERPROFILE\Downloads\python-3.12.0-amd64.exe"

    # Download the Python installer
    Invoke-WebRequest -Uri $pythonInstallerUrl -OutFile $pythonInstallerPath

    # Run the Python installer
    Start-Process -Wait -FilePath $pythonInstallerPath -ArgumentList "/quiet", "InstallAllUsers=1", "PrependPath=1"
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "The latest version of Python has been installed successfully."
    } else {
        Write-Host "Error installing the latest version of Python."
    }
}

function Verificar-Python {
    $pythonPath = "C:\Program Files\Python312"
    
    if (!(Test-Path $pythonPath)) {
        Instalar-PythonMaisRecente
    } else {
        Write-Host "Python is already installed."
    }
}

function Verificar-PythonNoPath {
    $pythonPath = "C:\Program Files\Python312"
    $pathFolders = $env:PATH -split ';'

    $pythonNotInPath = -not ($pathFolders -contains $pythonPath)

    if ($pythonNotInPath) {
        Write-Host "Python is not in the PATH. Adding Python to PATH..."

        $env:Path += ";$pythonPath"
        [Environment]::SetEnvironmentVariable("Path", $env:Path, [System.EnvironmentVariableTarget]::Machine)

        Write-Host "Python added to PATH successfully."
    } else {
        Write-Host "Python is already in the PATH."
    }
}

$pythonPath = "C:\Program Files\Python312"
$pipExe = Join-Path $pythonPath "Scripts\pip.exe"

function Verificar-Pip {
    if (-not (Test-Path -Path $pipExe)) {
        Write-Host "Pip is not installed. Installing Pip..."
        try {
            Start-Process -Wait -FilePath "$pythonPath\python.exe" -ArgumentList "-m", "ensurepip", "--default-pip"
            Write-Host "Pip has been installed successfully."
        } catch {
            Write-Host "Erro ao instalar Pip: $_"
        }
    } else {
        Write-Host "Pip is already installed."
    }
}

$bibliotecas = @("wxPython", "netifaces", "python-dateutil", "pyPubSub", "ipaddr")

function Verificar-Bibliotecas($bibliotecas) {
    foreach ($biblioteca in $bibliotecas) {
        Write-Host "Installing $biblioteca..."
        $resultado = Start-Process -Wait -FilePath $pipExe -ArgumentList "install", $biblioteca -PassThru
        if ($resultado.ExitCode -eq 0) {
            Write-Host "$biblioteca was installed successfully."
        } else {
            Write-Host "Error installing $biblioteca."
            Write-Host $resultado.StandardError
        }
    }
}

Verificar-Python
Verificar-PythonNoPath
Verificar-Pip
Verificar-Bibliotecas $bibliotecas

$caminho_arquivo = Join-Path $env:USERPROFILE "Desktop\Vector_Clock-master\Vector Clock Launcher.exe"

if (Test-Path -Path $caminho_arquivo) {
    Write-Host "Running $caminho_arquivo with administrator privileges..."
    Start-Process -FilePath $caminho_arquivo -Verb RunAs
} else {
    Write-Host "Unable to find file to run."
}
