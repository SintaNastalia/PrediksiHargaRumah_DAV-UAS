document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('predictButton').addEventListener('click', function() {
        const bedroomInput = document.getElementById('bedroom');
        const bathroomInput = document.getElementById('bathroom');
        const carportInput = document.getElementById('carport');
        const land_areaInput = document.getElementById('land_area');
        const build_areaInput = document.getElementById('build_area');
        const typeInput = document.getElementById('type');
        const methodInput = document.getElementById('method');

        const bedroom = parseInt(bedroomInput.value);
        const bathroom = parseInt(bathroomInput.value);
        const carport = parseInt(carportInput.value);
        const land_area = parseInt(land_areaInput.value);
        const build_area = parseInt(build_areaInput.value);
        const type = typeInput.value;
        const method = methodInput.value;

        const errorMessage = document.getElementById('error-message');

        // Validasi input tidak boleh kosong
        if (!bedroomInput.value || !bathroomInput.value || !carportInput.value || !land_areaInput.value || !build_areaInput.value) {
            errorMessage.textContent = "Semua field harus diisi.";
            errorMessage.style.display = 'block';
            return;
        }

        if (bedroom <= 0 || bathroom <= 0 ) {
            errorMessage.textContent = "Jumlah kamar tidur dan kamar mandi harus lebih dari 0.";
            errorMessage.style.display = 'block';
            return;
        } else if (land_area < 50 || build_area < 50) {
            errorMessage.textContent = "Luas tanah dan luas bangunan harus lebih dari 50.";
            errorMessage.style.display = 'block';
            return;
        } else if (carport < 0) {
            errorMessage.textContent = "Jumlah carport tidak boleh negatif.";
            errorMessage.style.display = 'block';
            return;
        } else if (bedroom > 8 || bathroom > 8 ) {
            errorMessage.textContent = "Jumlah kamar tidur dan kamar mandi tidak boleh lebih dari 8.";
            errorMessage.style.display = 'block';
            return;
        } else if (land_area > 700 || build_area > 700) {
            errorMessage.textContent = "Luas tanah dan luas bangunan tidak boleh lebih dari 700.";
            errorMessage.style.display = 'block';
            return;
        } else if (land_area < build_area) {
            errorMessage.textContent = "Luas tanah harus lebih besar dari luas bangunan.";
            errorMessage.style.display = 'block';
            return;
        } else {
            console.log('else block executed'); // Tambahkan log ini
            errorMessage.style.display = 'none';
            
            const successMessage = document.getElementById('successMessage');
            const methodInput = document.getElementById('method');
            let method = methodInput.value; // Dapatkan nilai dari methodInput
            
            method = method.replace(/_/g, ' '); // Ganti underscore dengan spasi
            
            successMessage.style.display = 'block';
            successMessage.textContent = `Data berhasil diprediksi menggunakan metode ${method}! Silahkan arahkan kursor ke peta untuk melihat harga per lokasi`;
        }

        const type_villa = type === 'villa' ? 1 : 0;
        const type_rumah = type === 'rumah' ? 1 : 0;

        const data = {
            bedroom: bedroom,
            bathroom: bathroom,
            carport: carport,
            land_area: land_area,
            build_area: build_area,
            type_villa: type_villa,
            type_rumah: type_rumah,
            method: method
        };

        fetch('http://localhost:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(predictions => {
            console.log('Predictions received:', predictions);
            updateMapWithPredictions(predictions);
        })
        .catch(error => console.error('Error:', error));
    });

    function updateMapWithPredictions(predictions) {
        console.log('Updating map with predictions:', predictions);
        const svgObject = document.getElementById("mapBali");

        svgObject.addEventListener('load', function() {
            console.log('SVG document loaded');

            const svgDoc = svgObject.contentDocument;
            if (!svgDoc) {
                console.error('SVG document is not accessible');
                return;
            }

            const svg = svgDoc.querySelector('svg');
            if (!svg) {
                console.error('SVG element is not accessible');
                return;
            }

            console.log('SVG is accessible:', svg);

            const handleElement = (element, kabupaten, price) => {
                const formattedPrice = price.toLocaleString('en-US'); // Format harga

                element.setAttribute("data-price", formattedPrice);

                element.addEventListener("mouseover", function(event) {
                    console.log(`Mouse over element for ${kabupaten}`);
                    const tooltip = document.getElementById('tooltip');
                    tooltip.innerHTML = `Kabupaten: ${kabupaten}<br>Prediksi Harga: ${formattedPrice}`;
                    tooltip.style.display = 'block';

                    const updateTooltipPosition = function(event) {
                        console.log(`Cursor position: ${event.pageX}, ${event.pageY}`);
                        tooltip.style.left = `${event.pageX + 5}px`;
                        tooltip.style.top = `${event.pageY + 5}px`;
                    };

                    document.addEventListener('mousemove', updateTooltipPosition);

                    element.addEventListener("mouseout", function() {
                        const tooltip = document.getElementById('tooltip');
                        tooltip.style.display = 'none';
                        element.style.fill = ''; // Kembali ke warna asli
                        document.removeEventListener('mousemove', updateTooltipPosition);
                    }, { once: true });

                    element.style.fill = '#00008B'; // Warna biru tua saat hover
                });
            };

            const paths = svg.querySelectorAll("path, g");
            console.log('Elements found in SVG:', paths);

            paths.forEach(element => {
                const kabupaten = element.id;
                console.log(`Processing element with ID: ${kabupaten}`);

                if (predictions.hasOwnProperty(kabupaten)) {
                    const price = predictions[kabupaten];
                    console.log(`Setting data-price for ${kabupaten} to ${price}`);

                    if (element.tagName === 'g') {
                        element.querySelectorAll('path').forEach(path => {
                            handleElement(path, kabupaten, price);
                        });
                    } else {
                        handleElement(element, kabupaten, price);
                    }
                } else {
                    console.warn(`No prediction found for kabupaten: ${kabupaten}`);
                }
            });
        });

        if (svgObject.contentDocument) {
            const event = new Event('load');
            svgObject.dispatchEvent(event);
        }
    }
});
