param (
    [string]$archivePath,
    [int]$rating
)

# Get the output directory (the same folder where the archive is located)
$outputDirectory = Split-Path -Path $archivePath


# Write-Output $archivePath > "C:\Users\ZT\Documents\_) Programs\Batch-Programs\Python-Windows-Star-Rating-Context-Assigner\Examples\test1.txt"
# Write-Output $rating > "C:\Users\ZT\Documents\_) Programs\Batch-Programs\Python-Windows-Star-Rating-Context-Assigner\Examples\test2.txt"

python "C:\Users\ZT\Documents\_) Programs\Batch-Programs\Python-Windows-Star-Rating-Context-Assigner\star_setter.py" --file $archivePath --rating $rating
