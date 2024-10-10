import React, { useState } from 'react';
import './product.css'; // Import CSS file for styling
import Layout from '@theme/Layout';

function AllParametersForm() {
    const [output, setOutput] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setIsLoading(true);
        const formData = new FormData(e.target);
        const object = {};
        formData.forEach(function(value, key){
            object[key] = value;
        });
        const json = JSON.stringify(object);
        // Simulate API call delay
        await new Promise(resolve => setTimeout(resolve, 6000)); // Set to 6 seconds
        setOutput('{"rf_bandgap": 3.593572, "rf_stability": true}'); // Default output
        setIsLoading(false);
    };


    return (
      <Layout>
        <div className='container_for_product'>
            <h1>Solarly Tool</h1>
            <div className='maincontainer'>
                <form onSubmit={handleSubmit} className='productcontainer'>
                    <div className='inputContainer'>
                        <label htmlFor="element_1" className='inputLabel'>Element 1:</label>
                        <input type="text" id="element_1" name="element_1" className='input' placeholder="e.g. Ac" />
                    </div>

                    <div className='inputContainer'>
                        <label htmlFor="element_2" className='inputLabel'>Element 2:</label>
                        <input type="text" id="element_2" name="element_2" className='input' placeholder="e.g. Al" />
                    </div>

                    <div className='inputContainer'>
                        <label htmlFor="element_3" className='inputLabel'>Element 3:</label>
                        <input type="text" id="element_3" name="element_3" className='input' placeholder="e.g. O" />
                    </div>

                    <div className='inputContainer'>
                        <label htmlFor="abc_str" className='inputLabel'>ABC:</label>
                        <input type="text" id="abc_str" name="abc_str" className='input' placeholder="e.g. 3.85,3.85,3.85" />
                    </div>

                    <div className='inputContainer'>
                        <label htmlFor="angles_str" className='inputLabel'>Angles:</label>
                        <input type="text" id="angles_str" name="angles_str" className='input' placeholder='e.g. 90,90,90' />
                    </div>

                    <div className='inputContainer'>
                        <label htmlFor="volume" className='inputLabel'>Volume:</label>
                        <input type="text" id="volume" name="volume" className='input' placeholder="e.g. 57.45" />
                    </div>

                    <div className='inputContainer'>
                        <label htmlFor="matrix_str" className='inputLabel'>Matrix:</label>
                        <input type="text" id="matrix_str" name="matrix_str" className='input' placeholder="e.g. 3.86,0.0,0.0,0.0,3.86,0.0,0.0,0.0,3.86" />
                    </div>

                    <div className='inputContainer'>
                        <label htmlFor="pbc_str" className='inputLabel'>PBC:</label>
                        <input type="text" id="pbc_str" name="pbc_str" className='input' placeholder="e.g. 1,1,1" />
                    </div>

                    <div className='inputContainer'>
                        <label htmlFor="frac_coords_1_str" className='inputLabel'>Frac Coords 1:</label>
                        <input type="text" id="frac_coords_1_str" name="frac_coords_1_str" className='input' placeholder="e.g. 0,0,0" />
                    </div>

                    <div className='inputContainer'>
                        <label htmlFor="frac_coords_2_str" className='inputLabel'>Frac Coords 2:</label>
                        <input type="text" id="frac_coords_2_str" name="frac_coords_2_str" className='input' placeholder="e.g. 0.5,0."/>
                    </div>

                    <div className='inputContainer'>
                        <label htmlFor="frac_coords_3_str" className='inputLabel'>Frac Coords 3:</label>
                        <input type="text" id="frac_coords_3_str" name="frac_coords_3_str" className='input' placeholder='e.g. 0.5,0.5,0' />
                    </div>

                    <div className='inputContainer'>
                        <label htmlFor="frac_coords_4_str" className='inputLabel'>Frac Coords 4:</label>
                        <input type="text" id="frac_coords_4_str" name="frac_coords_4_str" className='input' placeholder='e.g. 0.5,0,0.5' />
                    </div>

                    <div className='inputContainer'>
                        <label htmlFor="frac_coords_5_str" className='inputLabel'>Frac Coords 5:</label>
                        <input type="text" id="frac_coords_5_str" name="frac_coords_5_str" className='input' placeholder='e.g. 0,0.5,0.5' />
                    </div>

                    <input type="submit" value="Submit" className="submitButton" />
                    </form>
                    {isLoading && (
                        <div className="loading-container">
                            <div className="loading-circle"></div>
                        </div>
                    )}
                    {!isLoading && output && (
                        <div className='output-box'>
                            <h2>Output</h2>
                            <textarea 
                                value={output} 
                                rows={10} 
                                cols={50} 
                                readOnly 
                                className="output-textarea"
                                style={{ resize: 'none' }}
                            />
                        </div>
                    )}
                </div>
            </div>
        </Layout>
    );
}

export default AllParametersForm;