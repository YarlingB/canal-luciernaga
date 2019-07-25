import { environment } from '../../../environments/environment'

const apiEndPoint: string = environment.apiEndPoint;

export const Global = {
    url: apiEndPoint
};  